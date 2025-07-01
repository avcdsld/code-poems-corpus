function(target, name, contentLocation, manifest, packager, instrumentation) {
				var pushReq = {};

				if (name)
					pushReq.Name = name;

				if (contentLocation)
					pushReq.ContentLocation = contentLocation;

				if (target)
					pushReq.Target = target;

				if(manifest)
					pushReq.Manifest = manifest;

				if(packager)
					pushReq.Packager = packager;

				if(instrumentation)
					pushReq.Instrumentation = instrumentation;

				return this._xhrV1("PUT", require.toUrl("cfapi/apps"), pushReq);
			}