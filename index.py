import importlib

SOURCE_NAME = 'example'
PROCESSOR_NAME = 'example'
REPORT_NAME = 'example'

sourceModule = importlib.import_module(f'source.{SOURCE_NAME}')
processorModule = importlib.import_module(f'processor.{PROCESSOR_NAME}')
reportModule = importlib.import_module(f'report.{REPORT_NAME}')

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
reportModule.Report().generate(data)
print('\n-------------- End\n')

print('===========================================================\n')