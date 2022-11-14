let view;
let iframe;

function setMarkdownTemplate(name) {
  async function fetchTemplate(name) {
    const response = await fetch("/template/" + name);
    const text = await response.text();
    return text;
  }

  addEventListener("DOMContentLoaded", (event) => {
    const CM = window.CM;
    iframe = document.getElementById("theiframe");


    fetchTemplate(name).then((text) => {
      window.setMarkdown(text);
    });
  }

  function updateiframe() {
    const value = view.state.doc.toString();
    const uri_component = window.LZString144.compressToEncodedURIComponent(value);

    try {
      iframe.setAttribute("src", "/render?q=" + uri_component);
    } catch {}
  }

  function debounce(func, timeout = 300) {
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        func.apply(this, args);
      }, timeout);
    };
  }
  const updateiframeDebounced = debounce(updateiframe, 500);

  window.addEventListener("keydown", (e) => {
    updateiframeDebounced();
  });

  view = new CM.codemirror.EditorView({
    parent: document.getElementById("editor"),
  });

  function setMarkdown(doc) {
    view.setState(
      CM["@codemirror/state"].EditorState.create({
        doc: doc,
        extensions: [
          CM.codemirror.basicSetup,
          CM["@codemirror/view"].EditorView.lineWrapping,
          CM["@codemirror/view"].keymap.of([
            CM["@codemirror/lang-markdown"].markdown,
            CM["@codemirror/commands"].indentWithTab,
            // {key: "Ctrl-Enter", run: () => run()}
          ]),
        ],
      })
    );
    updateiframe();
  }
  window.setMarkdown = setMarkdown;
  setMarkdownTemplate("default");
});stener("keydown", e => {
  updateiframeDebounced();
});