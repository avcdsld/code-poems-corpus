def _random_mutation_operator(self, individual, allow_shrink=True):
        """Perform a replacement, insertion, or shrink mutation on an individual.

        Parameters
        ----------
        individual: DEAP individual
            A list of pipeline operators and model parameters that can be
            compiled by DEAP into a callable function

        allow_shrink: bool (True)
            If True the `mutShrink` operator, which randomly shrinks the pipeline,
            is allowed to be chosen as one of the random mutation operators.
            If False, `mutShrink`  will never be chosen as a mutation operator.

        Returns
        -------
        mut_ind: DEAP individual
            Returns the individual with one of the mutations applied to it

        """
        if self.tree_structure:
            mutation_techniques = [
                partial(gp.mutInsert, pset=self._pset),
                partial(mutNodeReplacement, pset=self._pset)
            ]
            # We can't shrink pipelines with only one primitive, so we only add it if we find more primitives.
            number_of_primitives = sum([isinstance(node, deap.gp.Primitive) for node in individual])
            if number_of_primitives > 1 and allow_shrink:
                mutation_techniques.append(partial(gp.mutShrink))
        else:
            mutation_techniques = [partial(mutNodeReplacement, pset=self._pset)]

        mutator = np.random.choice(mutation_techniques)

        unsuccesful_mutations = 0
        for _ in range(self._max_mut_loops):
            # We have to clone the individual because mutator operators work in-place.
            ind = self._toolbox.clone(individual)
            offspring, = mutator(ind)
            if str(offspring) not in self.evaluated_individuals_:
                # Update statistics
                # crossover_count is kept the same as for the predecessor
                # mutation count is increased by 1
                # predecessor is set to the string representation of the individual before mutation
                # generation is set to 'INVALID' such that we can recognize that it should be updated accordingly
                offspring.statistics['crossover_count'] = individual.statistics['crossover_count']
                offspring.statistics['mutation_count'] = individual.statistics['mutation_count'] + 1
                offspring.statistics['predecessor'] = (str(individual),)
                offspring.statistics['generation'] = 'INVALID'
                break
            else:
                unsuccesful_mutations += 1

        # Sometimes you have pipelines for which every shrunk version has already been explored too.
        # To still mutate the individual, one of the two other mutators should be applied instead.
        if ((unsuccesful_mutations == 50) and
           (type(mutator) is partial and mutator.func is gp.mutShrink)):
            offspring, = self._random_mutation_operator(individual, allow_shrink=False)

        return offspring,