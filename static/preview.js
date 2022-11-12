async function fetchTemplate(name) {
  const response = await fetch('/template/' + name)
  const text = await response.text()
  return text
}

function setMarkdown(name) {
    fetchTemplate(name).then(text => {
      window.view.dispatch({
      changes: {from: 0, insert: text}
    })
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
      "/render?q=" + window.LZString144.compressToEncodedURIComponent(value)
    )
  } catch {}
}

const updateiframe = debounce(_updateiframe, 500)

function run() {
  console.log("Run()ning...")
  updateiframe(document.getElementById('theiframe'))
}

window.addEventListener("keydown", e => {
  if (e.keyCode == 13) {
    run();
    e.preventDefault();
  }
});