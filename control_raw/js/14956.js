function() {
	var scriptJs = Ext.getCmp('scriptAreaId').getValue();
	var serverId = Ext.getCmp('serverComId').getValue();

	if (!serverId) {
		alert('serverId is required!');
		return;
	}

	window.parent.client.request('scripts', {
		command: 'run',
		serverId: serverId,
		script: scriptJs
	}, function(err, msg) {
		if (err) {
			alert(err);
			return;
		}
		Ext.getCmp('tesultTextId').setValue(msg);
	});
}