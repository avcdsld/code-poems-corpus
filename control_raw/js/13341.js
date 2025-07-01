function(/**string*/ outDir, /**string*/ fileName, /**string*/ content) {
		fs.writeFileSync(outDir + "/" + fileName, content, IO.encoding);
	}