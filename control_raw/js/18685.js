function exit()
{
	console.log("Exiting");

	myMotorShield_obj = null;
	if (MotorShield_lib)
	{
		MotorShield_lib.cleanUp();
		MotorShield_lib = null;
	}
	process.exit(0);
}