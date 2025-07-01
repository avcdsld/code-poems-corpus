def search_learning_rate(trainer: Trainer,
                         start_lr: float = 1e-5,
                         end_lr: float = 10,
                         num_batches: int = 100,
                         linear_steps: bool = False,
                         stopping_factor: float = None) -> Tuple[List[float], List[float]]:
    """
    Runs training loop on the model using :class:`~allennlp.training.trainer.Trainer`
    increasing learning rate from ``start_lr`` to ``end_lr`` recording the losses.
    Parameters
    ----------
    trainer: :class:`~allennlp.training.trainer.Trainer`
    start_lr: ``float``
        The learning rate to start the search.
    end_lr: ``float``
        The learning rate upto which search is done.
    num_batches: ``int``
        Number of batches to run the learning rate finder.
    linear_steps: ``bool``
        Increase learning rate linearly if False exponentially.
    stopping_factor: ``float``
        Stop the search when the current loss exceeds the best loss recorded by
        multiple of stopping factor. If ``None`` search proceeds till the ``end_lr``
    Returns
    -------
    (learning_rates, losses): ``Tuple[List[float], List[float]]``
        Returns list of learning rates and corresponding losses.
        Note: The losses are recorded before applying the corresponding learning rate
    """
    if num_batches <= 10:
        raise ConfigurationError('The number of iterations for learning rate finder should be greater than 10.')

    trainer.model.train()

    num_gpus = len(trainer._cuda_devices) # pylint: disable=protected-access

    raw_train_generator = trainer.iterator(trainer.train_data,
                                           shuffle=trainer.shuffle)
    train_generator = lazy_groups_of(raw_train_generator, num_gpus)
    train_generator_tqdm = Tqdm.tqdm(train_generator,
                                     total=num_batches)

    learning_rates = []
    losses = []
    best = 1e9
    if linear_steps:
        lr_update_factor = (end_lr - start_lr) / num_batches
    else:
        lr_update_factor = (end_lr / start_lr) ** (1.0 / num_batches)

    for i, batch_group in enumerate(train_generator_tqdm):

        if linear_steps:
            current_lr = start_lr + (lr_update_factor * i)
        else:
            current_lr = start_lr * (lr_update_factor ** i)

        for param_group in trainer.optimizer.param_groups:
            param_group['lr'] = current_lr

        trainer.optimizer.zero_grad()
        loss = trainer.batch_loss(batch_group, for_training=True)
        loss.backward()
        loss = loss.detach().cpu().item()

        if stopping_factor is not None and (math.isnan(loss) or loss > stopping_factor * best):
            logger.info(f'Loss ({loss}) exceeds stopping_factor * lowest recorded loss.')
            break

        trainer.rescale_gradients()
        trainer.optimizer.step()

        learning_rates.append(current_lr)
        losses.append(loss)

        if loss < best and i > 10:
            best = loss

        if i == num_batches:
            break

    return learning_rates, losses