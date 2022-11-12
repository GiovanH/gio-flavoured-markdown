async function fetchTemplate(name) {
  const response = await fetch('/template/' + name)
  const text = await response.text()
  return text
}

function setMarkdown(name) {
  fetchTemplate(name).then(text => {
    mdArea.value = text // todo transaction on view
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

function _updateiframe(iframe) {
  const value = window.view.state.doc.toString()
  try {
    iframe.setAttribute(
      'src', 
      "/render?q=" + LZString144.compressToEncodedURIComponent(value)
    )
  } catch {}
}

const updateiframe = debounce(_updateiframe, 500)

function run() {
  view
  updateiframe(theiframe)
}

window.addEventListener("keydown", e => {
  if (e.keyCode == 13 && (e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey) {
    run();
    e.preventDefault();
  }
});