def run(self, input_dir, output_dir, epsilon):
    """Runs attack inside Docker.

    Args:
      input_dir: directory with input (dataset).
      output_dir: directory where output (adversarial images) should be written.
      epsilon: maximum allowed size of adversarial perturbation,
        should be in range [0, 255].
    """
    print('Running attack ', self.name)
    cmd = [self.docker_binary(), 'run',
           '-v', '{0}:/input_images'.format(input_dir),
           '-v', '{0}:/output_images'.format(output_dir),
           '-v', '{0}:/code'.format(self.directory),
           '-w', '/code',
           self.container,
           './' + self.entry_point,
           '/input_images',
           '/output_images',
           str(epsilon)]
    print(' '.join(cmd))
    subprocess.call(cmd)