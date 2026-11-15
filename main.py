# tiny-chess v3b: 0x88 alpha-beta engine, 100k nodes/move + null-move pruning.
# The engine is lzma-packed in engine.lzma (same code as the measured v3b-100k).
import lzma, os
exec(lzma.decompress(open(os.path.join(os.path.dirname(__file__), "engine.lzma"), "rb").read()))
