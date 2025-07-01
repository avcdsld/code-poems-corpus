function manyToManyDescriptor(
    declaredFromModelName,
    declaredToModelName,
    throughModelName,
    throughFields,
    reverse
) {
    return {
        get() {
            const {
                session: {
                    [declaredFromModelName]: DeclaredFromModel,
                    [declaredToModelName]: DeclaredToModel,
                    [throughModelName]: ThroughModel,
                },
            } = this.getClass();

            const ThisModel = reverse
                ? DeclaredToModel
                : DeclaredFromModel;
            const OtherModel = reverse
                ? DeclaredFromModel
                : DeclaredToModel;

            const thisReferencingField = reverse
                ? throughFields.to
                : throughFields.from;
            const otherReferencingField = reverse
                ? throughFields.from
                : throughFields.to;

            const thisId = this.getId();

            const throughQs = ThroughModel.filter({
                [thisReferencingField]: thisId,
            });

            /**
             * all IDs of instances of the other model that are
             * referenced by any instance of the current model
             */
            const referencedOtherIds = new Set(
                throughQs
                    .toRefArray()
                    .map(obj => obj[otherReferencingField])
            );

            /**
             * selects all instances of other model that are referenced
             * by any instance of the current model
             */
            const qs = OtherModel.filter(otherModelInstance => (
                referencedOtherIds.has(
                    otherModelInstance[OtherModel.idAttribute]
                )
            ));

            /**
             * Allows adding OtherModel instances to be referenced by the current instance.
             *
             * E.g. Book.first().authors.add(1, 2) would add the authors with IDs 1 and 2
             * to the first book's list of referenced authors.
             *
             * @return undefined
             */
            qs.add = function add(...entities) {
                const idsToAdd = new Set(
                    entities.map(normalizeEntity)
                );

                const existingQs = throughQs.filter(through => (
                    idsToAdd.has(through[otherReferencingField])
                ));

                if (existingQs.exists()) {
                    const existingIds = existingQs
                        .toRefArray()
                        .map(through => through[otherReferencingField]);

                    throw new Error(`Tried to add already existing ${OtherModel.modelName} id(s) ${existingIds} to the ${ThisModel.modelName} instance with id ${thisId}`);
                }

                idsToAdd.forEach((id) => {
                    ThroughModel.create({
                        [otherReferencingField]: id,
                        [thisReferencingField]: thisId,
                    });
                });
            };

            /**
             * Removes references to all OtherModel instances from the current model.
             *
             * E.g. Book.first().authors.clear() would cause the first book's list
             * of referenced authors to become empty.
             *
             * @return undefined
             */
            qs.clear = function clear() {
                throughQs.delete();
            };

            /**
             * Removes references to all passed OtherModel instances from the current model.
             *
             * E.g. Book.first().authors.remove(1, 2) would cause the authors with
             * IDs 1 and 2 to no longer be referenced by the first book.
             *
             * @return undefined
             */
            qs.remove = function remove(...entities) {
                const idsToRemove = new Set(
                    entities.map(normalizeEntity)
                );

                const entitiesToDelete = throughQs.filter(
                    through => idsToRemove.has(through[otherReferencingField])
                );

                if (entitiesToDelete.count() !== idsToRemove.size) {
                    // Tried deleting non-existing entities.
                    const entitiesToDeleteIds = entitiesToDelete
                        .toRefArray()
                        .map(through => through[otherReferencingField]);

                    const unexistingIds = [...idsToRemove].filter(
                        id => !entitiesToDeleteIds.includes(id)
                    );

                    throw new Error(`Tried to delete non-existing ${OtherModel.modelName} id(s) ${unexistingIds} from the ${ThisModel.modelName} instance with id ${thisId}`);
                }

                entitiesToDelete.delete();
            };

            return qs;
        },

        set() {
            throw new Error('Tried setting a M2M field. Please use the related QuerySet methods add, remove and clear.');
        },
    };
}