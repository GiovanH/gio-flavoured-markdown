window.addEventListener("DOMContentLoaded", (event) => {
  const CM = window.CM;
  const iframe = document.getElementById("theiframe");

  function updateiframe() {
    const value = view.state.doc.toString();
    const uri_component =
      window.LZString144.compressToEncodedURIComponent(value);

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

  const view = new CM.codemirror.EditorView({
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

  function setMarkdownTemplate(name) {
    setMarkdown(`Loading ${name}...`);
    async function fetchTemplate(name) {
      const response = await fetch("/template/" + name);
      const text = await response.text();
      return text;
    }
    fetchTemplate(name).then((text) => {
      setMarkdown(text);
    });
  }
  window.setMarkdownTemplate = setMarkdownTemplate;

  setMarkdownTemplate("default");
});