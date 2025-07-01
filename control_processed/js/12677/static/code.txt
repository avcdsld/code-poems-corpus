function time() {
  let t = new Date().toString().split(' ');

  return {
    current: Date.now(),
    uptime: os.uptime(),
    timezone: (t.length >= 7) ? t[5] : '',
    timezoneName: (t.length >= 7) ? t.slice(6).join(' ').replace(/\(/g, '').replace(/\)/g, '') : ''
  };
}