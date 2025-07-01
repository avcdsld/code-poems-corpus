@Override
	public void open(int taskNumber, int numTasks) throws IOException {

		// enforce sequential open() calls
		synchronized (OPEN_MUTEX) {
			if (Integer.toString(taskNumber + 1).length() > 6) {
				throw new IOException("Task id too large.");
			}

			this.taskNumber = taskNumber + 1;

			// for hadoop 2.2
			this.configuration.set("mapreduce.output.basename", "tmp");

			TaskAttemptID taskAttemptID = TaskAttemptID.forName("attempt__0000_r_"
					+ String.format("%" + (6 - Integer.toString(taskNumber + 1).length()) + "s", " ").replace(" ", "0")
					+ Integer.toString(taskNumber + 1)
					+ "_0");

			this.configuration.set("mapred.task.id", taskAttemptID.toString());
			this.configuration.setInt("mapred.task.partition", taskNumber + 1);
			// for hadoop 2.2
			this.configuration.set("mapreduce.task.attempt.id", taskAttemptID.toString());
			this.configuration.setInt("mapreduce.task.partition", taskNumber + 1);

			try {
				this.context = new TaskAttemptContextImpl(this.configuration, taskAttemptID);
				this.outputCommitter = this.mapreduceOutputFormat.getOutputCommitter(this.context);
				this.outputCommitter.setupJob(new JobContextImpl(this.configuration, new JobID()));
			} catch (Exception e) {
				throw new RuntimeException(e);
			}

			this.context.getCredentials().addAll(this.credentials);
			Credentials currentUserCreds = getCredentialsFromUGI(UserGroupInformation.getCurrentUser());
			if (currentUserCreds != null) {
				this.context.getCredentials().addAll(currentUserCreds);
			}

			// compatible for hadoop 2.2.0, the temporary output directory is different from hadoop 1.2.1
			if (outputCommitter instanceof FileOutputCommitter) {
				this.configuration.set("mapreduce.task.output.dir", ((FileOutputCommitter) this.outputCommitter).getWorkPath().toString());
			}

			try {
				this.recordWriter = this.mapreduceOutputFormat.getRecordWriter(this.context);
			} catch (InterruptedException e) {
				throw new IOException("Could not create RecordWriter.", e);
			}
		}
	}