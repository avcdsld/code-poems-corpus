def get_hosted_zone_id_for_domain(self, domain):
        """
        Get the Hosted Zone ID for a given domain.

        """
        all_zones = self.get_all_zones()
        return self.get_best_match_zone(all_zones, domain)