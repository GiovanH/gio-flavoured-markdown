
function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}

function _updateiframe(mdArea, iframe_id) {
  try {
    document.getElementById(iframe_id).setAttribute(
      'src', 
      "/render?q=" + encodeURIComponent(LZString144.compressToBase64(mdArea.value))
    )
  } catch {}
}

const updateiframe = debounce(_updateiframe, 500)
