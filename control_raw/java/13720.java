public static void main(final String[] args) {
        new SpringApplicationBuilder(CasCommandLineShellApplication.class)
            .banner(new DefaultCasBanner())
            .bannerMode(Banner.Mode.CONSOLE)
            .logStartupInfo(true)
            .web(WebApplicationType.NONE)
            .run(args);
    }