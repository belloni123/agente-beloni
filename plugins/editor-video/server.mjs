import { isAbsolute, join } from "node:path";
import { pathToFileURL } from "node:url";

const editorRoot = process.env.EDITOR_VIDEO_ROOT;

if (!editorRoot || !isAbsolute(editorRoot)) {
  throw new Error("Configure EDITOR_VIDEO_ROOT com o caminho absoluto do Editor de Vídeo local.");
}

await import(pathToFileURL(join(editorRoot, "scripts", "mcp.mjs")).href);
