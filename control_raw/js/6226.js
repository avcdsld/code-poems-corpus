function getAriaQueryAttributes() {
				const ariaKeys = Array.from(props).map(([key]) => key);
				const roleAriaKeys = Array.from(roles).reduce((out, [name, rule]) => {
					return [...out, ...Object.keys(rule.props)];
				}, []);
				return new Set(axe.utils.uniqueArray(roleAriaKeys, ariaKeys));
			}