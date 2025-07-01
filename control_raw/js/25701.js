function build() {
	if (process.versions.electron) {
		args.push('--target='+ process.versions.electron,  '--dist-url=https://atom.io/download/atom-shell');
	}
	cp.spawn(
		process.platform === 'win32' ? 'node-gyp.cmd' : 'node-gyp',
		['rebuild'].concat(args),
		{stdio: [process.stdin, process.stdout, process.stderr]})
	.on('exit', function(err) {
		if (err) {
			console.error(
				'node-gyp exited with code: '+ err+ '\n'+
				'Please make sure you are using a supported platform and node version. If you\n'+
				'would like to compile fibers on this machine please make sure you have setup your\n'+
				'build environment--\n'+
				'Windows + OS X instructions here: https://github.com/nodejs/node-gyp\n'+
				'Ubuntu users please run: `sudo apt-get install g++ build-essential`\n'+
				'RHEL users please run: `yum install gcc-c++` and `yum groupinstall \'Development Tools\'` \n'+
				'Alpine users please run: `sudo apk add python make g++`'
			);
			return process.exit(err);
		}
		afterBuild();
	})
	.on('error', function(err) {
		console.error(
			'node-gyp not found! Please ensure node-gyp is in your PATH--\n'+
			'Try running: `sudo npm install -g node-gyp`'
		);
		console.log(err.message);
		process.exit(1);
	});
}