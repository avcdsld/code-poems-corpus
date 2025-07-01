function CircularRegion (identifier, latitude, longitude, radius){
	// Call the parent constructor, making sure (using Function#call)
	// that "this" is set correctly during the call
	Region.call(this, identifier);

	CircularRegion.checkLatitude(latitude);
	CircularRegion.checkLongitude(longitude);
	CircularRegion.checkRadius(radius);

	this.latitude = latitude;
	this.longitude = longitude;
	this.radius = radius;

	// {String} typeName A String holding the name of the Objective-C type that the value
	//    this will get converted to once the data is in the Objective-C runtime.
	this.typeName = 'CircularRegion';
  
}