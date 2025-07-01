function create() {
		// Check form for errors
		if(!$("#privateKey").val() || !$("#recipient").val()) return alert('Missing parameter !');
		if(undefined === $("#amount").val() || !nem.utils.helpers.isTextAmountValid($("#amount").val())) return alert('Invalid amount !');
		if (!nem.model.address.isValid(nem.model.address.clean($("#recipient").val()))) return alert('Invalid recipent address !');

		// Set the private key in common object
		common.privateKey = $("#privateKey").val();

		// Check private key for errors
		if (common.privateKey.length !== 64 && common.privateKey.length !== 66) return alert('Invalid private key, length must be 64 or 66 characters !');
    	if (!nem.utils.helpers.isHexadecimal(common.privateKey)) return alert('Private key must be hexadecimal only !');

		// Set the cleaned amount into transfer transaction object
		transferTransaction.amount = nem.utils.helpers.cleanTextAmount($("#amount").val());

		// Recipient address must be clean (no hypens: "-")
		transferTransaction.recipient = nem.model.address.clean($("#recipient").val());

		// Set message
		transferTransaction.message = $("#message").val();

		// Prepare the updated transfer transaction object
		var transactionEntity = nem.model.transactions.prepare("transferTransaction")(common, transferTransaction, nem.model.network.data.testnet.id);

		// Create a key pair object from private key
		var kp = nem.crypto.keyPair.create(nem.utils.helpers.fixPrivateKey(common.privateKey));

		// Serialize the transaction
		var serialized = nem.utils.serialization.serializeTransaction(transactionEntity);

		// Sign the serialized transaction with keypair object
	    var signature = kp.sign(serialized);

	    // Build the object to send
	    var result = {
	        'data': nem.utils.convert.ua2hex(serialized),
	        'signature': signature.toString()
	    };

	    // Show the object to send in view
	    $("#result").val(JSON.stringify(result));
	}