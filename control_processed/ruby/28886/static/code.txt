def create_set(hostnames, opts={})
       hostnames ||= []
       
       ld "Creating set from:", hostnames.inspect
       
       opts = {
         :user => (current_machine_user).to_s,
         :parallel => @@global.parallel,
         :quiet => Rudy.quiet?
       }.merge(opts)
       set = ::Rye::Set.new current_machine_group, opts 
       
       opts.delete(:parallel)   # Not used by Rye::Box.new

       hostnames.each do |m| 

         if m.is_a?(Rudy::Machine)
           m.refresh! if m.dns_public.nil? || m.dns_public.empty?
           if m.dns_public.nil? || m.dns_public.empty?
             ld "Cannot find public DNS for #{m.name} (continuing...)"
             rbox = self.create_box('nohost', opts) 
           else
             ld [:dns_public, m.dns_public, m.instid]
             rbox = self.create_box(m.dns_public, opts) 
           end
           rbox.stash = m   # Store the machine instance in the stash
           rbox.nickname = m.name
         else
           # Otherwise we assume it's a hostname
           rbox = self.create_box(m)
         end
         rbox.add_key user_keypairpath(opts[:user])
         set.add_box rbox
       end

       ld "Machines Set: %s" % [set.empty? ? '[empty]' : set.inspect]

       set
     end