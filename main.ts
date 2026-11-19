// Entry program for the make.fun bounty gta6-meme-x-01 (Node 22, standard
// library only). The entry itself is a post on X; this repository only has
// to hand the house the post's address. So the whole job here is: take
// POST.json from the repository root and place an exact copy of it in the
// output directory, where the grader reads it.
//
// The grader sets MAKEFUN_BOT_DIR (the repository) and MAKEFUN_OUTPUT_DIR
// (the output). Run locally the same way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// The copy is byte for byte and the program consults nothing else -- no
// network, no clock, no randomness -- so two runs always agree.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoDir = process.env.MAKEFUN_BOT_DIR ?? dirname(fileURLToPath(import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(repoDir, "POST.json");
const targetPath = join(outputDir, "POST.json");

function fail(stage: string, cause: unknown): never {
  console.error(`${stage}: ${(cause as Error).message}`);
  process.exit(1);
}

// Refuse to hand over a file that is not the JSON object the gate expects;
// a broken POST.json fails here, in the open, instead of at the gate.
function assertPostFile(payload: Buffer): void {
  const parsed: unknown = JSON.parse(payload.toString("utf8"));
  const url = (parsed as { url?: unknown } | null)?.url;
  if (typeof parsed !== "object" || parsed === null || typeof url !== "string" || url.length === 0) {
    throw new Error("POST.json must be a JSON object with a non-empty string url");
  }
}

let payload: Buffer;
try {
  payload = readFileSync(sourcePath);
} catch (cause) {
  fail(`cannot read ${sourcePath}`, cause);
}
try {
  assertPostFile(payload!);
} catch (cause) {
  fail(`invalid ${sourcePath}`, cause);
}

try {
  mkdirSync(outputDir, { recursive: true });
  writeFileSync(targetPath, payload!);
} catch (cause) {
  fail(`cannot write ${targetPath}`, cause);
}
