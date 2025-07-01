function Albers(params) {
    //http://pubs.er.usgs.gov/djvu/PP/PP_1395.pdf, page 101 &  292
    //for NAD_1983_Alaska_Albers: LatLng()<  === > Point();
    params = params || {};
  SpatialReference.call(this, params);
    var f_i = params.inverse_flattening;
    var phi1 = params.standard_parallel_1 * RAD_DEG;
    var phi2 = params.standard_parallel_2 * RAD_DEG;
    var phi0 = params.latitude_of_origin * RAD_DEG;
    this.a_ = params.semi_major / params.unit;
    this.lamda0_ = params.central_meridian * RAD_DEG;
    this.FE_ = params.false_easting;
    this.FN_ = params.false_northing;
    
    var f = 1.0 / f_i; //e: eccentricity of the ellipsoid where e^2  =  2f - f^2 
    var es = 2 * f - f * f;
    this.e_ = Math.sqrt(es);
    var m1 = this.calc_m_(phi1, es);
    var m2 = this.calc_m_(phi2, es);
    
    var q1 = this.calc_q_(phi1, this.e_);
    var q2 = this.calc_q_(phi2, this.e_);
    var q0 = this.calc_q_(phi0, this.e_);
    
    this.n_ = (m1 * m1 - m2 * m2) / (q2 - q1);
    this.C_ = m1 * m1 + this.n_ * q1;
    this.rho0_ = this.calc_rho_(this.a_, this.C_, this.n_, q0);
}