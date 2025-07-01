function(obj, variable)
{
	var codec = new mxObjectCodec(obj,  ['model', 'previous'], ['cell']);

	/**
	 * Function: afterDecode
	 *
	 * Restores the state by assigning the previous value.
	 */
	codec.afterDecode = function(dec, node, obj)
	{
		// Allows forward references in sessions. This is a workaround
		// for the sequence of edits in mxGraph.moveCells and cellsAdded.
		if (mxUtils.isNode(obj.cell))
		{
			obj.cell = dec.decodeCell(obj.cell, false);
		}

		obj.previous = obj[variable];

		return obj;
	};
	
	return codec;
}