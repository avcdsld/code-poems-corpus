function binfile( ...files ) {

    for ( const file of files ) {

        if ( fs.existsSync( file ) ) return file;

    }

    throw `Could not find: ${ files.join( " || " ) }`;

}