import importlib

NAME = 'example'

sourceModule = importlib.import_module(f'src.{NAME}.source')
processorModule = importlib.import_module(f'src.{NAME}.processor')
reportModule = importlib.import_module(f'src.{NAME}.report')

print('===========================================================\n')

print('Querying ...')
data = sourceModule.Source().query()
print('Source: ----------\n')
print(data)
print('\n-------------- End\n')

print('===========================================================\n')

print('Processing ...')
results = processorModule.Processor().process(data)
print('Result: ----------\n')
print(results)
print('\n-------------- End\n')

print('===========================================================\n')

print('Report: ----------\n')
reportModule.Report().generate(results)
print('\n-------------- End\n')

print('===========================================================\n')