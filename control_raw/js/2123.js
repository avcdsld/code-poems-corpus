function(lines) {
		let output = [];
		let newlineCount = 0;
		for (let i = 0; i < lines.length; i++) {
			const line = lines[i];
			if (!line.trim()) {
				newlineCount++;
			} else {
				newlineCount = 0;
			}

			if (newlineCount >= 2) continue;

			output.push(line);
		}
		return output;
	}