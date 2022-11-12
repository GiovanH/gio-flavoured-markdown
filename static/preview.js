async function fetchTemplate(name) {
  const response = await fetch('/template/' + name)
  const text = await response.text()
  return text
}

function setMarkdownTemplate(name) {
  fetchTemplate(name).then(text => {
    window.setMarkdown(text)
  });
}

function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}

function updateiframe() {
  const iframe = document.getElementById('theiframe')
  const value = window.view.state.doc.toString()
  try {
    iframe.setAttribute(
      'src', 
      "/render?q=" + window.LZString144.compressToEncodedURIComponent(value)
    )
  } catch {}
}

const updateiframeDebounced = debounce(updateiframe, 500)

window.addEventListener("keydown", e => {
  updateiframeDebounced();
});