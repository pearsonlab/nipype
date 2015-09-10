# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.diffusion.gtract import gtractResampleCodeImage

def test_gtractResampleCodeImage_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputCodeVolume=dict(argstr='--inputCodeVolume %s',
    ),
    inputReferenceVolume=dict(argstr='--inputReferenceVolume %s',
    ),
    inputTransform=dict(argstr='--inputTransform %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    transformType=dict(argstr='--transformType %s',
    ),
    )
    inputs = gtractResampleCodeImage.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_gtractResampleCodeImage_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = gtractResampleCodeImage.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

