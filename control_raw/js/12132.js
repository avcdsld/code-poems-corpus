function attachPriceIndustryDurationKeyToBid(bid, brandCategoryExclusion) {
  let initialCacheKey = bidCacheRegistry.getInitialCacheKey(bid);
  let duration = utils.deepAccess(bid, 'video.durationBucket');
  let cpmFixed = bid.cpm.toFixed(2);
  let pcd;

  if (brandCategoryExclusion) {
    let category = utils.deepAccess(bid, 'meta.adServerCatId');
    pcd = `${cpmFixed}_${category}_${duration}s`;
  } else {
    pcd = `${cpmFixed}_${duration}s`;
  }

  if (!bid.adserverTargeting) {
    bid.adserverTargeting = {};
  }
  bid.adserverTargeting[TARGETING_KEY_PB_CAT_DUR] = pcd;
  bid.adserverTargeting[TARGETING_KEY_CACHE_ID] = initialCacheKey;
  bid.videoCacheKey = initialCacheKey;
  bid.customCacheKey = `${pcd}_${initialCacheKey}`;
}