function updateiframe(mdArea, iframe_id) {
  try {
  document.getElementById(iframe_id).setAttribute('src', "/render?q=" + encodeURIComponent(mdArea.value))
  } catch {}
}