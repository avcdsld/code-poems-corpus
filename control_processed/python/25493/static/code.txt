def delete_firewall_rule(self, firewall_rule):
        '''
        Deletes the specified firewall rule
        '''
        firewall_rule_id = self._find_firewall_rule_id(firewall_rule)
        ret = self.network_conn.delete_firewall_rule(firewall_rule_id)
        return ret if ret else True