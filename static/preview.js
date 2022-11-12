async function fetchTemplate(name) {
  const response = await fetch('/template/' + name)
  const text = await response.text()
  return text
}

function setMarkdown(mdArea, name) {
  fetchTemplate(name).then(text => {
    mdArea.value = text
    mdArea.oninput()
  });
}

function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}

function _updateiframe(mdArea, iframe) {
  try {
    iframe.setAttribute(
      'src', 
      "/render?q=" + LZString144.compressToEncodedURIComponent(mdArea.value)
    )
  } catch {}
}

const updateiframe = debounce(_updateiframe, 500)
