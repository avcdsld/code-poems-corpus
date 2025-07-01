def create_trap_vb_list(sys_up_time, trap_oid, object_list)
      vb_args = @mib.varbind_list(object_list, :KeepValue)
      uptime_vb = VarBind.new(SNMP::SYS_UP_TIME_OID, TimeTicks.new(sys_up_time.to_int))
      trap_vb = VarBind.new(SNMP::SNMP_TRAP_OID_OID, @mib.oid(trap_oid))
      VarBindList.new([uptime_vb, trap_vb, *vb_args])
    end