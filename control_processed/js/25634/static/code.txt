async function _getPresignedPosts(siteId, checksums) {
  const endpoint = url.resolve(apiURL, `/sites/${siteId}/presigned_posts`);
  const body = { checksums };
  const response = await got.post(endpoint, { body, json: true, headers: _bearer() });

  return response.body.presignedPosts;
}