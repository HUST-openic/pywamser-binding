from wasmer import engine, Store, Module, Instance, wat2wasm
from wasmer_compiler_cranelift import Compiler

store = Store()
u
wasm_bytes = wat2wasm(
    """
    (module
      (type $add_one_t (func (param i32) (result i32)))
      (func $add_one_f (type $add_one_t) (param $value i32) (result i32)
        local.get $value
        i32.const 1
        i32.add)
      (export "add_one" (func $add_one_f)))
    """
)

engine = engine.JIT(Compiler)
store = Store(engine)
module = Module(store, wasm_bytes)

instance = Instance(module)