# node-iconv

Text recoding in JavaScript for fun and profit!

## Installing

If you are developing against node.js v0.3.0:

	npm install iconv@0.3.0

If you are developing against the older but stable node.js v0.2.x:

    npm install iconv@0.2.0

Both versions of node.js are fully supported. Once v0.3.0 goes stable,
support for v0.2.x will be slowly phased out but it will receive
bug fixes and minor updates for the foreseeable future.

## Usage

Encode from one character encoding to another:

	// convert from UTF-8 to ISO-8859-1
	var Buffer = require('buffer').Buffer;
	var Iconv  = require('iconv').Iconv;
	var assert = require('assert');
	
	var iconv = new Iconv('UTF-8', 'ISO-8859-1');
	var buffer = iconv.convert('Hello, world!');
	var buffer2 = iconv.convert(new Buffer('Hello, world!'));
	assert.equals(buffer.inspect(), buffer2.inspect());
	// do something useful with the buffers

Look at `tests/test.js` for more examples and node-iconv's behaviour under error conditions.

## Notes

Things to keep in mind when you work with node-iconv.

### Chunked data

Say you are reading data in chunks from a HTTP stream. The logical input is a single document (the full POST request data) but the physical input will be spread over several buffers (the request chunks).

You must accumulate the small buffers into a single large buffer before performing the conversion. If you don't, you will get unexpected results with multi-byte and stateful character sets like UTF-8 and ISO-2022-JP.

[node-buffertools](http://github.com/bnoordhuis/node-buffertools) lets you concatenate buffers painlessly. See the description of `buffertools.concat()` for details.

### EINVAL

EINVAL is raised when the input ends in a partial character sequence. This is a feature,
not a bug.
