function inflate(data, usz) {
	/* shortcircuit for empty buffer [0x03, 0x00] */
	if(data[0] == 3 && !(data[1] & 0x3)) { return [new_raw_buf(usz), 2]; }

	/* bit offset */
	var boff = 0;

	/* header includes final bit and type bits */
	var header = 0;

	var outbuf = new_unsafe_buf(usz ? usz : (1<<18));
	var woff = 0;
	var OL = outbuf.length>>>0;
	var max_len_1 = 0, max_len_2 = 0;

	while((header&1) == 0) {
		header = read_bits_3(data, boff); boff += 3;
		if((header >>> 1) == 0) {
			/* Stored block */
			if(boff & 7) boff += 8 - (boff&7);
			/* 2 bytes sz, 2 bytes bit inverse */
			var sz = data[boff>>>3] | data[(boff>>>3)+1]<<8;
			boff += 32;
			/* push sz bytes */
			if(!usz && OL < woff + sz) { outbuf = realloc(outbuf, woff + sz); OL = outbuf.length; }
			if(typeof data.copy === 'function') {
				// $FlowIgnore
				data.copy(outbuf, woff, boff>>>3, (boff>>>3)+sz);
				woff += sz; boff += 8*sz;
			} else while(sz-- > 0) { outbuf[woff++] = data[boff>>>3]; boff += 8; }
			continue;
		} else if((header >>> 1) == 1) {
			/* Fixed Huffman */
			max_len_1 = 9; max_len_2 = 5;
		} else {
			/* Dynamic Huffman */
			boff = dyn(data, boff);
			max_len_1 = dyn_len_1; max_len_2 = dyn_len_2;
		}
		if(!usz && (OL < woff + 32767)) { outbuf = realloc(outbuf, woff + 32767); OL = outbuf.length; }
		for(;;) { // while(true) is apparently out of vogue in modern JS circles
			/* ingest code and move read head */
			var bits = read_bits_n(data, boff, max_len_1);
			var code = (header>>>1) == 1 ? fix_lmap[bits] : dyn_lmap[bits];
			boff += code & 15; code >>>= 4;
			/* 0-255 are literals, 256 is end of block token, 257+ are copy tokens */
			if(((code>>>8)&0xFF) === 0) outbuf[woff++] = code;
			else if(code == 256) break;
			else {
				code -= 257;
				var len_eb = (code < 8) ? 0 : ((code-4)>>2); if(len_eb > 5) len_eb = 0;
				var tgt = woff + LEN_LN[code];
				/* length extra bits */
				if(len_eb > 0) {
					tgt += read_bits_n(data, boff, len_eb);
					boff += len_eb;
				}

				/* dist code */
				bits = read_bits_n(data, boff, max_len_2);
				code = (header>>>1) == 1 ? fix_dmap[bits] : dyn_dmap[bits];
				boff += code & 15; code >>>= 4;
				var dst_eb = (code < 4 ? 0 : (code-2)>>1);
				var dst = DST_LN[code];
				/* dist extra bits */
				if(dst_eb > 0) {
					dst += read_bits_n(data, boff, dst_eb);
					boff += dst_eb;
				}

				/* in the common case, manual byte copy is faster than TA set / Buffer copy */
				if(!usz && OL < tgt) { outbuf = realloc(outbuf, tgt); OL = outbuf.length; }
				while(woff < tgt) { outbuf[woff] = outbuf[woff - dst]; ++woff; }
			}
		}
	}
	return [usz ? outbuf : outbuf.slice(0, woff), (boff+7)>>>3];
}