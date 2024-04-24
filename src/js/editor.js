import EditorJS from "@editorjs/editorjs";
import Header from "@editorjs/header";
import List from '@editorjs/list';
import Embed from '@editorjs/embed';
import Link from '@editorjs/link'

const editor = new EditorJS({
  holder: 'editorjs',
  autofocus: true,
  tools: {
    header: Header,
    list: List,
    embed: Embed,
    linkTool: {
      class: Link,
      config: {
        endpoint: 'http://localhost:8000/fetchurl',
      }
    }
  }
});