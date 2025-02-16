## SpecStory

## Untitled (16/02/2025, 21:27:19)

_**User**_

Run `sh ./02-check.sh`, then implement the @TODO.md instructions in priority order & fix what fails. The edit the @LOG.md to report on what you've done, then run `sh ./03-up.sh` fix & retry. Occasionally adjust @README.md to more accurately describe the project as it is, and update @TODO.md 

---

_**Assistant**_

I'll help you with this task. Let's start by running the check script to see what needs attention.

---

_****_

```bash
sh ./02-check.sh
```

```
│   │   ├── gzip.data.json
│   │   ├── gzip.meta.json
│   │   ├── importlib
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _abc.data.json
│   │   │   ├── _abc.meta.json
│   │   │   ├── _bootstrap.data.json
│   │   │   ├── _bootstrap.meta.json
│   │   │   ├── _bootstrap_external.data.json
│   │   │   ├── _bootstrap_external.meta.json
│   │   │   ├── abc.data.json
│   │   │   ├── abc.meta.json
│   │   │   ├── machinery.data.json
│   │   │   ├── machinery.meta.json
│   │   │   ├── metadata
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _meta.data.json
│   │   │   │   └── _meta.meta.json
│   │   │   ├── readers.data.json
│   │   │   ├── readers.meta.json
│   │   │   ├── resources
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _common.data.json
│   │   │   │   ├── _common.meta.json
│   │   │   │   ├── abc.data.json
│   │   │   │   ├── abc.meta.json
│   │   │   │   ├── readers.data.json
│   │   │   │   └── readers.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── iniconfig
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _parse.data.json
│   │   │   ├── _parse.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   └── exceptions.meta.json
│   │   ├── inspect.data.json
│   │   ├── inspect.meta.json
│   │   ├── io.data.json
│   │   ├── io.meta.json
│   │   ├── itertools.data.json
│   │   ├── itertools.meta.json
│   │   ├── json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── decoder.data.json
│   │   │   ├── decoder.meta.json
│   │   │   ├── encoder.data.json
│   │   │   └── encoder.meta.json
│   │   ├── keyword.data.json
│   │   ├── keyword.meta.json
│   │   ├── locale.data.json
│   │   ├── locale.meta.json
│   │   ├── logging
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── markdown
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── blockparser.data.json
│   │   │   ├── blockparser.meta.json
│   │   │   ├── blockprocessors.data.json
│   │   │   ├── blockprocessors.meta.json
│   │   │   ├── core.data.json
│   │   │   ├── core.meta.json
│   │   │   ├── extensions
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── codehilite.data.json
│   │   │   │   ├── codehilite.meta.json
│   │   │   │   ├── fenced_code.data.json
│   │   │   │   ├── fenced_code.meta.json
│   │   │   │   ├── meta.data.json
│   │   │   │   ├── meta.meta.json
│   │   │   │   ├── tables.data.json
│   │   │   │   ├── tables.meta.json
│   │   │   │   ├── toc.data.json
│   │   │   │   └── toc.meta.json
│   │   │   ├── inlinepatterns.data.json
│   │   │   ├── inlinepatterns.meta.json
│   │   │   ├── postprocessors.data.json
│   │   │   ├── postprocessors.meta.json
│   │   │   ├── preprocessors.data.json
│   │   │   ├── preprocessors.meta.json
│   │   │   ├── treeprocessors.data.json
│   │   │   ├── treeprocessors.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── marshal.data.json
│   │   ├── marshal.meta.json
│   │   ├── math.data.json
│   │   ├── math.meta.json
│   │   ├── mmap.data.json
│   │   ├── mmap.meta.json
│   │   ├── multiprocessing
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── connection.data.json
│   │   │   ├── connection.meta.json
│   │   │   ├── context.data.json
│   │   │   ├── context.meta.json
│   │   │   ├── managers.data.json
│   │   │   ├── managers.meta.json
│   │   │   ├── pool.data.json
│   │   │   ├── pool.meta.json
│   │   │   ├── popen_fork.data.json
│   │   │   ├── popen_fork.meta.json
│   │   │   ├── popen_forkserver.data.json
│   │   │   ├── popen_forkserver.meta.json
│   │   │   ├── popen_spawn_posix.data.json
│   │   │   ├── popen_spawn_posix.meta.json
│   │   │   ├── popen_spawn_win32.data.json
│   │   │   ├── popen_spawn_win32.meta.json
│   │   │   ├── process.data.json
│   │   │   ├── process.meta.json
│   │   │   ├── queues.data.json
│   │   │   ├── queues.meta.json
│   │   │   ├── reduction.data.json
│   │   │   ├── reduction.meta.json
│   │   │   ├── shared_memory.data.json
│   │   │   ├── shared_memory.meta.json
│   │   │   ├── sharedctypes.data.json
│   │   │   ├── sharedctypes.meta.json
│   │   │   ├── spawn.data.json
│   │   │   ├── spawn.meta.json
│   │   │   ├── synchronize.data.json
│   │   │   ├── synchronize.meta.json
│   │   │   ├── util.data.json
│   │   │   └── util.meta.json
│   │   ├── numbers.data.json
│   │   ├── numbers.meta.json
│   │   ├── numpy
│   │   │   ├── __config__.data.json
│   │   │   ├── __config__.meta.json
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _array_api_info.data.json
│   │   │   ├── _array_api_info.meta.json
│   │   │   ├── _core
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _asarray.data.json
│   │   │   │   ├── _asarray.meta.json
│   │   │   │   ├── _internal.data.json
│   │   │   │   ├── _internal.meta.json
│   │   │   │   ├── _type_aliases.data.json
│   │   │   │   ├── _type_aliases.meta.json
│   │   │   │   ├── _ufunc_config.data.json
│   │   │   │   ├── _ufunc_config.meta.json
│   │   │   │   ├── arrayprint.data.json
│   │   │   │   ├── arrayprint.meta.json
│   │   │   │   ├── defchararray.data.json
│   │   │   │   ├── defchararray.meta.json
│   │   │   │   ├── einsumfunc.data.json
│   │   │   │   ├── einsumfunc.meta.json
│   │   │   │   ├── fromnumeric.data.json
│   │   │   │   ├── fromnumeric.meta.json
│   │   │   │   ├── function_base.data.json
│   │   │   │   ├── function_base.meta.json
│   │   │   │   ├── multiarray.data.json
│   │   │   │   ├── multiarray.meta.json
│   │   │   │   ├── numeric.data.json
│   │   │   │   ├── numeric.meta.json
│   │   │   │   ├── numerictypes.data.json
│   │   │   │   ├── numerictypes.meta.json
│   │   │   │   ├── records.data.json
│   │   │   │   ├── records.meta.json
│   │   │   │   ├── shape_base.data.json
│   │   │   │   ├── shape_base.meta.json
│   │   │   │   ├── strings.data.json
│   │   │   │   └── strings.meta.json
│   │   │   ├── _expired_attrs_2_0.data.json
│   │   │   ├── _expired_attrs_2_0.meta.json
│   │   │   ├── _globals.data.json
│   │   │   ├── _globals.meta.json
│   │   │   ├── _pytesttester.data.json
│   │   │   ├── _pytesttester.meta.json
│   │   │   ├── _typing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _add_docstring.data.json
│   │   │   │   ├── _add_docstring.meta.json
│   │   │   │   ├── _array_like.data.json
│   │   │   │   ├── _array_like.meta.json
│   │   │   │   ├── _callable.data.json
│   │   │   │   ├── _callable.meta.json
│   │   │   │   ├── _char_codes.data.json
│   │   │   │   ├── _char_codes.meta.json
│   │   │   │   ├── _dtype_like.data.json
│   │   │   │   ├── _dtype_like.meta.json
│   │   │   │   ├── _extended_precision.data.json
│   │   │   │   ├── _extended_precision.meta.json
│   │   │   │   ├── _nbit.data.json
│   │   │   │   ├── _nbit.meta.json
│   │   │   │   ├── _nbit_base.data.json
│   │   │   │   ├── _nbit_base.meta.json
│   │   │   │   ├── _nested_sequence.data.json
│   │   │   │   ├── _nested_sequence.meta.json
│   │   │   │   ├── _scalars.data.json
│   │   │   │   ├── _scalars.meta.json
│   │   │   │   ├── _shape.data.json
│   │   │   │   ├── _shape.meta.json
│   │   │   │   ├── _ufunc.data.json
│   │   │   │   └── _ufunc.meta.json
│   │   │   ├── _utils
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _convertions.data.json
│   │   │   │   └── _convertions.meta.json
│   │   │   ├── char
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── core
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── ctypeslib.data.json
│   │   │   ├── ctypeslib.meta.json
│   │   │   ├── dtypes.data.json
│   │   │   ├── dtypes.meta.json
│   │   │   ├── exceptions.data.json
│   │   │   ├── exceptions.meta.json
│   │   │   ├── f2py
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── fft
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _helper.data.json
│   │   │   │   ├── _helper.meta.json
│   │   │   │   ├── _pocketfft.data.json
│   │   │   │   └── _pocketfft.meta.json
│   │   │   ├── lib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _array_utils_impl.data.json
│   │   │   │   ├── _array_utils_impl.meta.json
│   │   │   │   ├── _arraypad_impl.data.json
│   │   │   │   ├── _arraypad_impl.meta.json
│   │   │   │   ├── _arraysetops_impl.data.json
│   │   │   │   ├── _arraysetops_impl.meta.json
│   │   │   │   ├── _arrayterator_impl.data.json
│   │   │   │   ├── _arrayterator_impl.meta.json
│   │   │   │   ├── _datasource.data.json
│   │   │   │   ├── _datasource.meta.json
│   │   │   │   ├── _function_base_impl.data.json
│   │   │   │   ├── _function_base_impl.meta.json
│   │   │   │   ├── _histograms_impl.data.json
│   │   │   │   ├── _histograms_impl.meta.json
│   │   │   │   ├── _index_tricks_impl.data.json
│   │   │   │   ├── _index_tricks_impl.meta.json
│   │   │   │   ├── _nanfunctions_impl.data.json
│   │   │   │   ├── _nanfunctions_impl.meta.json
│   │   │   │   ├── _npyio_impl.data.json
│   │   │   │   ├── _npyio_impl.meta.json
│   │   │   │   ├── _polynomial_impl.data.json
│   │   │   │   ├── _polynomial_impl.meta.json
│   │   │   │   ├── _scimath_impl.data.json
│   │   │   │   ├── _scimath_impl.meta.json
│   │   │   │   ├── _shape_base_impl.data.json
│   │   │   │   ├── _shape_base_impl.meta.json
│   │   │   │   ├── _stride_tricks_impl.data.json
│   │   │   │   ├── _stride_tricks_impl.meta.json
│   │   │   │   ├── _twodim_base_impl.data.json
│   │   │   │   ├── _twodim_base_impl.meta.json
│   │   │   │   ├── _type_check_impl.data.json
│   │   │   │   ├── _type_check_impl.meta.json
│   │   │   │   ├── _ufunclike_impl.data.json
│   │   │   │   ├── _ufunclike_impl.meta.json
│   │   │   │   ├── _utils_impl.data.json
│   │   │   │   ├── _utils_impl.meta.json
│   │   │   │   ├── _version.data.json
│   │   │   │   ├── _version.meta.json
│   │   │   │   ├── array_utils.data.json
│   │   │   │   ├── array_utils.meta.json
│   │   │   │   ├── format.data.json
│   │   │   │   ├── format.meta.json
│   │   │   │   ├── introspect.data.json
│   │   │   │   ├── introspect.meta.json
│   │   │   │   ├── mixins.data.json
│   │   │   │   ├── mixins.meta.json
│   │   │   │   ├── npyio.data.json
│   │   │   │   ├── npyio.meta.json
│   │   │   │   ├── scimath.data.json
│   │   │   │   ├── scimath.meta.json
│   │   │   │   ├── stride_tricks.data.json
│   │   │   │   └── stride_tricks.meta.json
│   │   │   ├── linalg
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _linalg.data.json
│   │   │   │   └── _linalg.meta.json
│   │   │   ├── ma
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── core.data.json
│   │   │   │   ├── core.meta.json
│   │   │   │   ├── extras.data.json
│   │   │   │   ├── extras.meta.json
│   │   │   │   ├── mrecords.data.json
│   │   │   │   └── mrecords.meta.json
│   │   │   ├── matlib.data.json
│   │   │   ├── matlib.meta.json
│   │   │   ├── matrixlib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── defmatrix.data.json
│   │   │   │   └── defmatrix.meta.json
│   │   │   ├── polynomial
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _polybase.data.json
│   │   │   │   ├── _polybase.meta.json
│   │   │   │   ├── _polytypes.data.json
│   │   │   │   ├── _polytypes.meta.json
│   │   │   │   ├── chebyshev.data.json
│   │   │   │   ├── chebyshev.meta.json
│   │   │   │   ├── hermite.data.json
│   │   │   │   ├── hermite.meta.json
│   │   │   │   ├── hermite_e.data.json
│   │   │   │   ├── hermite_e.meta.json
│   │   │   │   ├── laguerre.data.json
│   │   │   │   ├── laguerre.meta.json
│   │   │   │   ├── legendre.data.json
│   │   │   │   ├── legendre.meta.json
│   │   │   │   ├── polynomial.data.json
│   │   │   │   ├── polynomial.meta.json
│   │   │   │   ├── polyutils.data.json
│   │   │   │   └── polyutils.meta.json
│   │   │   ├── random
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _generator.data.json
│   │   │   │   ├── _generator.meta.json
│   │   │   │   ├── _mt19937.data.json
│   │   │   │   ├── _mt19937.meta.json
│   │   │   │   ├── _pcg64.data.json
│   │   │   │   ├── _pcg64.meta.json
│   │   │   │   ├── _philox.data.json
│   │   │   │   ├── _philox.meta.json
│   │   │   │   ├── _sfc64.data.json
│   │   │   │   ├── _sfc64.meta.json
│   │   │   │   ├── bit_generator.data.json
│   │   │   │   ├── bit_generator.meta.json
│   │   │   │   ├── mtrand.data.json
│   │   │   │   └── mtrand.meta.json
│   │   │   ├── rec
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── strings
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── testing
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _private
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── utils.data.json
│   │   │   │   │   └── utils.meta.json
│   │   │   │   ├── overrides.data.json
│   │   │   │   └── overrides.meta.json
│   │   │   ├── typing
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── opcode.data.json
│   │   ├── opcode.meta.json
│   │   ├── operator.data.json
│   │   ├── operator.meta.json
│   │   ├── os
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── path.data.json
│   │   │   └── path.meta.json
│   │   ├── packaging
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _elffile.data.json
│   │   │   ├── _elffile.meta.json
│   │   │   ├── _manylinux.data.json
│   │   │   ├── _manylinux.meta.json
│   │   │   ├── _musllinux.data.json
│   │   │   ├── _musllinux.meta.json
│   │   │   ├── _parser.data.json
│   │   │   ├── _parser.meta.json
│   │   │   ├── _structures.data.json
│   │   │   ├── _structures.meta.json
│   │   │   ├── _tokenizer.data.json
│   │   │   ├── _tokenizer.meta.json
│   │   │   ├── markers.data.json
│   │   │   ├── markers.meta.json
│   │   │   ├── requirements.data.json
│   │   │   ├── requirements.meta.json
│   │   │   ├── specifiers.data.json
│   │   │   ├── specifiers.meta.json
│   │   │   ├── tags.data.json
│   │   │   ├── tags.meta.json
│   │   │   ├── utils.data.json
│   │   │   ├── utils.meta.json
│   │   │   ├── version.data.json
│   │   │   └── version.meta.json
│   │   ├── pathlib.data.json
│   │   ├── pathlib.meta.json
│   │   ├── pdb.data.json
│   │   ├── pdb.meta.json
│   │   ├── pickle.data.json
│   │   ├── pickle.meta.json
│   │   ├── pkg_resources
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   └── _vendored_packaging
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       ├── markers.data.json
│   │   │       ├── markers.meta.json
│   │   │       ├── requirements.data.json
│   │   │       ├── requirements.meta.json
│   │   │       ├── specifiers.data.json
│   │   │       ├── specifiers.meta.json
│   │   │       ├── version.data.json
│   │   │       └── version.meta.json
│   │   ├── pkgutil.data.json
│   │   ├── pkgutil.meta.json
│   │   ├── platform.data.json
│   │   ├── platform.meta.json
│   │   ├── pluggy
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _callers.data.json
│   │   │   ├── _callers.meta.json
│   │   │   ├── _hooks.data.json
│   │   │   ├── _hooks.meta.json
│   │   │   ├── _manager.data.json
│   │   │   ├── _manager.meta.json
│   │   │   ├── _result.data.json
│   │   │   ├── _result.meta.json
│   │   │   ├── _tracing.data.json
│   │   │   ├── _tracing.meta.json
│   │   │   ├── _version.data.json
│   │   │   ├── _version.meta.json
│   │   │   ├── _warnings.data.json
│   │   │   └── _warnings.meta.json
│   │   ├── posixpath.data.json
│   │   ├── posixpath.meta.json
│   │   ├── pprint.data.json
│   │   ├── pprint.meta.json
│   │   ├── py
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── error.data.json
│   │   │   ├── error.meta.json
│   │   │   ├── iniconfig.data.json
│   │   │   ├── iniconfig.meta.json
│   │   │   ├── io.data.json
│   │   │   ├── io.meta.json
│   │   │   ├── path.data.json
│   │   │   ├── path.meta.json
│   │   │   ├── xml.data.json
│   │   │   └── xml.meta.json
│   │   ├── pytest
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── queue.data.json
│   │   ├── queue.meta.json
│   │   ├── re.data.json
│   │   ├── re.meta.json
│   │   ├── reprlib.data.json
│   │   ├── reprlib.meta.json
│   │   ├── resource.data.json
│   │   ├── resource.meta.json
│   │   ├── selectors.data.json
│   │   ├── selectors.meta.json
│   │   ├── shlex.data.json
│   │   ├── shlex.meta.json
│   │   ├── shutil.data.json
│   │   ├── shutil.meta.json
│   │   ├── signal.data.json
│   │   ├── signal.meta.json
│   │   ├── socket.data.json
│   │   ├── socket.meta.json
│   │   ├── sre_compile.data.json
│   │   ├── sre_compile.meta.json
│   │   ├── sre_constants.data.json
│   │   ├── sre_constants.meta.json
│   │   ├── sre_parse.data.json
│   │   ├── sre_parse.meta.json
│   │   ├── ssl.data.json
│   │   ├── ssl.meta.json
│   │   ├── string.data.json
│   │   ├── string.meta.json
│   │   ├── struct.data.json
│   │   ├── struct.meta.json
│   │   ├── subprocess.data.json
│   │   ├── subprocess.meta.json
│   │   ├── sys
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _monitoring.data.json
│   │   │   └── _monitoring.meta.json
│   │   ├── sysconfig.data.json
│   │   ├── sysconfig.meta.json
│   │   ├── tarfile.data.json
│   │   ├── tarfile.meta.json
│   │   ├── tempfile.data.json
│   │   ├── tempfile.meta.json
│   │   ├── tests
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── textwrap.data.json
│   │   ├── textwrap.meta.json
│   │   ├── threading.data.json
│   │   ├── threading.meta.json
│   │   ├── time.data.json
│   │   ├── time.meta.json
│   │   ├── token.data.json
│   │   ├── token.meta.json
│   │   ├── tokenize.data.json
│   │   ├── tokenize.meta.json
│   │   ├── traceback.data.json
│   │   ├── traceback.meta.json
│   │   ├── twardown_py
│   │   │   ├── __init__.data.json
│   │   │   └── __init__.meta.json
│   │   ├── types.data.json
│   │   ├── types.meta.json
│   │   ├── typing.data.json
│   │   ├── typing.meta.json
│   │   ├── typing_extensions.data.json
│   │   ├── typing_extensions.meta.json
│   │   ├── unicodedata.data.json
│   │   ├── unicodedata.meta.json
│   │   ├── unittest
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _log.data.json
│   │   │   ├── _log.meta.json
│   │   │   ├── async_case.data.json
│   │   │   ├── async_case.meta.json
│   │   │   ├── case.data.json
│   │   │   ├── case.meta.json
│   │   │   ├── loader.data.json
│   │   │   ├── loader.meta.json
│   │   │   ├── main.data.json
│   │   │   ├── main.meta.json
│   │   │   ├── result.data.json
│   │   │   ├── result.meta.json
│   │   │   ├── runner.data.json
│   │   │   ├── runner.meta.json
│   │   │   ├── signals.data.json
│   │   │   ├── signals.meta.json
│   │   │   ├── suite.data.json
│   │   │   └── suite.meta.json
│   │   ├── uuid.data.json
│   │   ├── uuid.meta.json
│   │   ├── warnings.data.json
│   │   ├── warnings.meta.json
│   │   ├── weakref.data.json
│   │   ├── weakref.meta.json
│   │   ├── xml
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   └── etree
│   │   │       ├── ElementTree.data.json
│   │   │       ├── ElementTree.meta.json
│   │   │       ├── __init__.data.json
│   │   │       └── __init__.meta.json
│   │   ├── zipfile
│   │   │   ├── __init__.data.json
│   │   │   ├── __init__.meta.json
│   │   │   ├── _path.data.json
│   │   │   └── _path.meta.json
│   │   ├── zipimport.data.json
│   │   ├── zipimport.meta.json
│   │   ├── zlib.data.json
│   │   └── zlib.meta.json
│   └── CACHEDIR.TAG
├── .specstory
│   └── history
│       ├── .what-is-this.md
│       ├── executing-tasks-from-todo-file.md
│       ├── script-execution-and-error-handling.md
│       ├── script-execution-and-implementation-steps.md
│       ├── script-execution-and-robustness-improvement-1.md
│       ├── script-execution-and-robustness-improvement.md
│       ├── shell-script-execution-and-troubleshooting-1.md
│       ├── shell-script-execution-and-troubleshooting.md
│       └── task-organization-from-folder-contents.md
├── 01-firststeps.sh
├── 02-check.sh
├── 03-up.sh
├── LOG.md
├── README.md
├── TODO.md
├── create-github-repos.sh
├── tree.txt
├── twardown-docs
│   ├── .DS_Store
│   ├── .github
│   │   └── workflows
│   │       └── ci.yml
│   ├── .gitignore
│   ├── .markdownlint.json
│   ├── .prettierrc
│   ├── LICENSE
│   ├── LOG.md
│   ├── README.md
│   ├── dev
│   │   ├── 01-tests.md
│   │   ├── 02-twardown-js-01.md
│   │   ├── 03-twardown-js-02.md
│   │   ├── 04-remark-gfm-forreference.txt
│   │   └── contributing.md
│   ├── examples
│   │   └── basic.md
│   ├── guides
│   │   └── getting-started.md
│   ├── package-lock.json
│   ├── package.json
│   └── spec
│       └── index.md
├── twardown-js
│   ├── .babelrc
│   ├── .eslintrc.cjs
│   ├── .github
│   │   └── workflows
│   │       └── ci.yml
│   ├── .gitignore
│   ├── .husky
│   │   └── _
│   │       ├── .gitignore
│   │       ├── applypatch-msg
│   │       ├── commit-msg
│   │       ├── h
│   │       ├── husky.sh
│   │       ├── post-applypatch
│   │       ├── post-checkout
│   │       ├── post-commit
│   │       ├── post-merge
│   │       ├── post-rewrite
│   │       ├── pre-applypatch
│   │       ├── pre-auto-gc
│   │       ├── pre-commit
│   │       ├── pre-merge-commit
│   │       ├── pre-push
│   │       ├── pre-rebase
│   │       └── prepare-commit-msg
│   ├── LICENSE
│   ├── LOG.md
│   ├── README.md
│   ├── babel.config.js
│   ├── package-lock.json
│   ├── package.json
│   ├── src
│   │   └── index.js
│   └── test
│       └── index.test.js
├── twardown-py
│   ├── .coverage
│   ├── .github
│   │   └── workflows
│   │       └── ci.yml
│   ├── .gitignore
│   ├── .mypy_cache
│   │   ├── .gitignore
│   │   ├── 3.8
│   │   │   ├── @plugins_snapshot.json
│   │   │   ├── _ast.data.json
│   │   │   ├── _ast.meta.json
│   │   │   ├── _codecs.data.json
│   │   │   ├── _codecs.meta.json
│   │   │   ├── _collections_abc.data.json
│   │   │   ├── _collections_abc.meta.json
│   │   │   ├── _frozen_importlib.data.json
│   │   │   ├── _frozen_importlib.meta.json
│   │   │   ├── _frozen_importlib_external.data.json
│   │   │   ├── _frozen_importlib_external.meta.json
│   │   │   ├── _io.data.json
│   │   │   ├── _io.meta.json
│   │   │   ├── _sitebuiltins.data.json
│   │   │   ├── _sitebuiltins.meta.json
│   │   │   ├── _thread.data.json
│   │   │   ├── _thread.meta.json
│   │   │   ├── _typeshed
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── importlib.data.json
│   │   │   │   └── importlib.meta.json
│   │   │   ├── abc.data.json
│   │   │   ├── abc.meta.json
│   │   │   ├── ast.data.json
│   │   │   ├── ast.meta.json
│   │   │   ├── builtins.data.json
│   │   │   ├── builtins.meta.json
│   │   │   ├── codecs.data.json
│   │   │   ├── codecs.meta.json
│   │   │   ├── collections
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── abc.data.json
│   │   │   │   └── abc.meta.json
│   │   │   ├── contextlib.data.json
│   │   │   ├── contextlib.meta.json
│   │   │   ├── dataclasses.data.json
│   │   │   ├── dataclasses.meta.json
│   │   │   ├── email
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _policybase.data.json
│   │   │   │   ├── _policybase.meta.json
│   │   │   │   ├── charset.data.json
│   │   │   │   ├── charset.meta.json
│   │   │   │   ├── contentmanager.data.json
│   │   │   │   ├── contentmanager.meta.json
│   │   │   │   ├── errors.data.json
│   │   │   │   ├── errors.meta.json
│   │   │   │   ├── header.data.json
│   │   │   │   ├── header.meta.json
│   │   │   │   ├── message.data.json
│   │   │   │   ├── message.meta.json
│   │   │   │   ├── policy.data.json
│   │   │   │   └── policy.meta.json
│   │   │   ├── enum.data.json
│   │   │   ├── enum.meta.json
│   │   │   ├── genericpath.data.json
│   │   │   ├── genericpath.meta.json
│   │   │   ├── importlib
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── _bootstrap.data.json
│   │   │   │   ├── _bootstrap.meta.json
│   │   │   │   ├── _bootstrap_external.data.json
│   │   │   │   ├── _bootstrap_external.meta.json
│   │   │   │   ├── abc.data.json
│   │   │   │   ├── abc.meta.json
│   │   │   │   ├── machinery.data.json
│   │   │   │   ├── machinery.meta.json
│   │   │   │   └── metadata
│   │   │   │       ├── __init__.data.json
│   │   │   │       └── __init__.meta.json
│   │   │   ├── io.data.json
│   │   │   ├── io.meta.json
│   │   │   ├── logging
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── markdown
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── blockparser.data.json
│   │   │   │   ├── blockparser.meta.json
│   │   │   │   ├── blockprocessors.data.json
│   │   │   │   ├── blockprocessors.meta.json
│   │   │   │   ├── core.data.json
│   │   │   │   ├── core.meta.json
│   │   │   │   ├── extensions
│   │   │   │   │   ├── __init__.data.json
│   │   │   │   │   ├── __init__.meta.json
│   │   │   │   │   ├── codehilite.data.json
│   │   │   │   │   ├── codehilite.meta.json
│   │   │   │   │   ├── fenced_code.data.json
│   │   │   │   │   ├── fenced_code.meta.json
│   │   │   │   │   ├── meta.data.json
│   │   │   │   │   ├── meta.meta.json
│   │   │   │   │   ├── tables.data.json
│   │   │   │   │   ├── tables.meta.json
│   │   │   │   │   ├── toc.data.json
│   │   │   │   │   └── toc.meta.json
│   │   │   │   ├── inlinepatterns.data.json
│   │   │   │   ├── inlinepatterns.meta.json
│   │   │   │   ├── postprocessors.data.json
│   │   │   │   ├── postprocessors.meta.json
│   │   │   │   ├── preprocessors.data.json
│   │   │   │   ├── preprocessors.meta.json
│   │   │   │   ├── treeprocessors.data.json
│   │   │   │   ├── treeprocessors.meta.json
│   │   │   │   ├── util.data.json
│   │   │   │   └── util.meta.json
│   │   │   ├── os
│   │   │   │   ├── __init__.data.json
│   │   │   │   ├── __init__.meta.json
│   │   │   │   ├── path.data.json
│   │   │   │   └── path.meta.json
│   │   │   ├── pathlib.data.json
│   │   │   ├── pathlib.meta.json
│   │   │   ├── posixpath.data.json
│   │   │   ├── posixpath.meta.json
│   │   │   ├── re.data.json
│   │   │   ├── re.meta.json
│   │   │   ├── resource.data.json
│   │   │   ├── resource.meta.json
│   │   │   ├── signal.data.json
│   │   │   ├── signal.meta.json
│   │   │   ├── sre_compile.data.json
│   │   │   ├── sre_compile.meta.json
│   │   │   ├── sre_constants.data.json
│   │   │   ├── sre_constants.meta.json
│   │   │   ├── sre_parse.data.json
│   │   │   ├── sre_parse.meta.json
│   │   │   ├── string.data.json
│   │   │   ├── string.meta.json
│   │   │   ├── subprocess.data.json
│   │   │   ├── subprocess.meta.json
│   │   │   ├── sys
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── threading.data.json
│   │   │   ├── threading.meta.json
│   │   │   ├── time.data.json
│   │   │   ├── time.meta.json
│   │   │   ├── twardown_py
│   │   │   │   ├── __init__.data.json
│   │   │   │   └── __init__.meta.json
│   │   │   ├── types.data.json
│   │   │   ├── types.meta.json
│   │   │   ├── typing.data.json
│   │   │   ├── typing.meta.json
│   │   │   ├── typing_extensions.data.json
│   │   │   ├── typing_extensions.meta.json
│   │   │   └── xml
│   │   │       ├── __init__.data.json
│   │   │       ├── __init__.meta.json
│   │   │       └── etree
│   │   │           ├── ElementTree.data.json
│   │   │           ├── ElementTree.meta.json
│   │   │           ├── __init__.data.json
│   │   │           └── __init__.meta.json
│   │   └── CACHEDIR.TAG
│   ├── .pytest_cache
│   │   ├── .gitignore
│   │   ├── CACHEDIR.TAG
│   │   ├── README.md
│   │   └── v
│   │       └── cache
│   │           ├── lastfailed
│   │           ├── nodeids
│   │           └── stepwise
│   ├── .ruff_cache
│   │   ├── .gitignore
│   │   ├── 0.9.6
│   │   │   ├── 15250710585263566173
│   │   │   └── 4512268198192392240
│   │   └── CACHEDIR.TAG
│   ├── LICENSE
│   ├── LOG.md
│   ├── README.md
│   ├── coverage.xml
│   ├── pyproject.toml
│   ├── src
│   │   └── twardown_py
│   │       └── __init__.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_extension.py
│   └── update.log
└── update.log

103 directories, 1099 files
-e 
=== Python Package Status ===
-e Python version:
Python 3.12.8
-e Running tests:
Audited 1 package in 3ms
...../Users/adam/Developer/vcs/github.twardoch/pub/twardown-org/twardown-py/.
venv/lib/python3.12/site-packages/coverage/inorout.py:524: CoverageWarning: M
odule twardown_py was previously imported, but not measured (module-not-measu
red)
  self.warn(msg, slug="module-not-measured")
                                                                 [100%]

---------- coverage: platform darwin, python 3.12.8-final-0 ----------
Coverage XML written to file coverage.xml

5 passed in 0.35s
-e Running type checks:
Success: no issues found in 1 source file
-e Running linting:
All checks passed!
3 files already formatted
-e 
=== JavaScript Package Status ===
-e Node.js version:
v22.10.0
-e npm version:
11.1.0
-e Installing dependencies:

up to date, audited 502 packages in 2s

96 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
-e Running tests:

> twardown-js@0.1.0 test
> NODE_OPTIONS=--experimental-vm-modules jest

 FAIL  test/index.test.js
  ● Test suite failed to run

    ReferenceError: require is not defined

    > 1 | import { describe, expect, test } from '@jest/globals';
        | ^
      2 | import { unified } from 'unified'
      3 | import remarkParse from 'remark-parse'
      4 | import remarkStringify from 'remark-stringify'

      at require (test/index.test.js:1:1)

Test Suites: 1 failed, 1 total
Tests:       0 total
Snapshots:   0 total
Time:        0.557 s
Ran all test suites.
(node:54828) ExperimentalWarning: VM Modules is an experimental feature and m
ight change at any time
(Use `node --trace-warnings ...` to show where the warning was created)
-e Tests failed
-e Running linting:

> twardown-js@0.1.0 lint
> eslint src test


> twardown-js@0.1.0 format:check
> prettier --check '**/*.{js,jsx,ts,tsx,json,md}'

Checking formatting...
[warn] babel.config.js
[warn] LOG.md
[warn] src/index.js
[warn] test/index.test.js
[warn] Code style issues found in 4 files. Run Prettier with --write to fix.
-e Format check failed
-e 
=== Documentation Status ===
-e Installing dependencies:

up to date, audited 62 packages in 1s

20 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
-e Running Markdown linting:

> twardown-docs@0.1.0 lint
> markdownlint '**/*.md' --ignore node_modules

dev/01-tests.md:5 MD025/single-title/single-h1 Multiple top-level headings in
 the same document [Context: "# The Grand Theory of Antarcti..."]
dev/01-tests.md:35:1 MD004/ul-style Unordered list style [Expected: dash; Act
ual: asterisk]
dev/01-tests.md:44:31 MD034/no-bare-urls Bare URL used [Context: "https://exa
mple.com"]
dev/01-tests.md:44:1 MD052/reference-links-images Reference links and images 
should use a label that is defined [Missing link or image reference definitio
n: "ref"] [Context: "[Latest Findings][ref]"]
dev/02-twardown-js-01.md:9:29 MD034/no-bare-urls Bare URL used [Context: "htt
ps://github.com/remarkjs/re..."]
dev/02-twardown-js-01.md:36 MD028/no-blanks-blockquote Blank line inside bloc
kquote
dev/02-twardown-js-01.md:1233:3 MD034/no-bare-urls Bare URL used [Context: "h
ttps://marketplace.visualstud..."]
dev/02-twardown-js-01.md:1234:3 MD034/no-bare-urls Bare URL used [Context: "h
ttps://github.com/remarkjs/vs..."]
dev/03-twardown-js-02.md:29 MD031/blanks-around-fences Fenced code blocks sho
uld be surrounded by blank lines [Context: "```json"]
dev/03-twardown-js-02.md:887:1 MD030/list-marker-space Spaces after list mark
ers [Expected: 1; Actual: 2]
dev/03-twardown-js-02.md:892:1 MD030/list-marker-space Spaces after list mark
ers [Expected: 1; Actual: 2]
examples/basic.md:8 MD025/single-title/single-h1 Multiple top-level headings 
in the same document [Context: "# Basic Twardown Example"]
guides/getting-started.md:120 MD031/blanks-around-fences Fenced code blocks s
hould be surrounded by blank lines [Context: "```markdown"]
guides/getting-started.md:136 MD031/blanks-around-fences Fenced code blocks s
hould be surrounded by blank lines [Context: "```json"]
-e Markdown linting failed
-e Running format check:

> twardown-docs@0.1.0 format:check
> prettier --check '**/*.md'

Checking formatting...
All matched files use Prettier code style!
-e 
=== CI Status ===
-e Checking GitHub Actions status:
-e 
twardown-py:
STATUS  TITLE          WORKFLOW  BRANCH  EVENT  ID         ELAPSED  AGE      
✓       Update rep...  CI        main    push   133583...  23s      about ...
-e 
twardown-js:
STATUS  TITLE          WORKFLOW  BRANCH  EVENT  ID         ELAPSED  AGE      
X       Update rep...  CI        main    push   133583...  17s      about ...
-e 
twardown-docs:
STATUS  TITLE          WORKFLOW  BRANCH  EVENT  ID         ELAPSED  AGE      
X       Update rep...  CI        main    push   133584...  1m0s     about ...
-e 
twardown-org:
⣽
```

---

_****_



---



---

