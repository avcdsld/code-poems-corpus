function onResize() {
	if ( this.stdout.columns && this.stdout.rows ) {
		this.width = this.stdout.columns ;
		this.height = this.stdout.rows ;
	}

	this.emit( 'resize' , this.width , this.height ) ;
}