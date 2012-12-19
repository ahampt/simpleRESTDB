import cgi, json, logging, sys
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse, Http404
from webapp.models import Data

site_logger = logging.getLogger('log.site')
database_logger = logging.getLogger('log.database')

# Retrieve specific stored information by key
def get(request):
		if request.method == 'POST':
			'''*****************************************************************************
			Respond to JSON input with completed JSON output
			PATH: webapp.views.site.get - *See urls.py
			METHOD: post - *Required to get to function
			PARAMS: none - *Required to get to function
			MISC: none - *Required to get to function
			*****************************************************************************'''
			try:
				objs = json.loads(request.POST.items().pop()[0])
				result = {}
				for tuple in objs.items():
		                	if tuple[0] and tuple[1] == 'Key':
						try:
							result[tuple[0]] = Data.objects.get(Key=tuple[0]).Value
						except ObjectDoesNotExist:
							result[tuple[0]] = 'KeyNotFound'
				return HttpResponse(json.dumps(result).encode('utf-8'), mimetype='application/json')
			except Exception:
				exc_info = str(sys.exc_info()[0])
				site_logger.error('Unexpected error: ' + exc_info)
				return HttpResponse(cgi.escape('Unexpected error' + exc_info), mimetype=None, status=200)
		else:
			'''*****************************************************************************
			Display 404
			PATH: webapp.views.site.get; METHOD: not post; PARAMS: none; MISC: none;
			*****************************************************************************'''
			raise Http404

# Retrieve all stored information
def get_all(request):
		'''*****************************************************************************
		JSON reply with all key/value pairs in the database
		PATH: webapp.views.site.get_all; METHOD: none; PARAMS: none; MISC: none;
		*****************************************************************************'''
		try:
			result = {}
			for data in Data.objects.all():
				result[data.Key] = data.Value
			return HttpResponse(json.dumps(result).encode('utf-8'), mimetype='application/json')
		except Exception:
			exc_info = str(sys.exc_info()[0])
			site_logger.error('Unexpected error: ' + exc_info)
			return HttpResponse(cgi.escape('Unexpected error' + exc_info), mimetype=None, status=200)

# Store incoming data
def update(request):
		if request.method == 'POST':
			'''*****************************************************************************
			Update keys in JSON input and return status in JSON (with value on success and error message otherwise)
			PATH: webapp.views.site.update; METHOD: post; PARAMS: none; MISC: none;
			*****************************************************************************'''
			try:
				objs = json.loads(request.POST.items().pop()[0])
				result = {}
				for tuple in objs.items():
		                	if tuple[0] and tuple[1]:
						try:
							data = Data.objects.get(Key=tuple[0])
							data.Value = tuple[1]
							data.save()
							result[data.Key] = data.Value
							database_logger.info('Key: ' + data.Key + ' Value: ' + data.Value + ' Update Success')
						except ObjectDoesNotExist:
							data = Data(Key=tuple[0],Value=tuple[1])
							try:
								data.save()
								result[data.Key] = data.Value
								database_logger.info('Key: ' + data.Key + ' Value: ' + data.Value + ' Create Success')
							except ValidationError as e:
								database_logger.info('Key: ' + data.Key + ' Value: ' + data.Value + ' Update Failure')
								if len(e.message_dict.keys()) > 1:
									result[data.Key] = str(e.message_dict)
								else:
									result[data.Key] = str(e.message_dict[e.message_dict.keys[0]])
				return HttpResponse(json.dumps(result).encode('utf-8'), mimetype='application/json')
			except Exception:
				exc_info = str(sys.exc_info()[0])
				site_logger.error('Unexpected error: ' + exc_info)
				return HttpResponse(cgi.escape('Unexpected error' + exc_info), mimetype=None, status=200)
		else:
			'''*****************************************************************************
			Display 404
			PATH: webapp.views.site.update; METHOD: not post; PARAMS: none; MISC: none;
			*****************************************************************************'''
			raise Http404

# Delete specific key and associated value
def delete(request):
		if request.method == 'POST':
			'''*****************************************************************************
			Delete key/value entry in database
			PATH: webapp.views.site.delete; METHOD: post; PARAMS: none; MISC: none;
			*****************************************************************************'''
			try:
				objs = json.loads(request.POST.items().pop()[0])
				result = {}
				for tuple in objs.items():
		                	if tuple[0] and tuple[1] == 'Delete':
						try:
							Data.objects.get(Key=tuple[0]).delete()
							result[tuple[0]] = 'Deleted'
							database_logger.info('Key: ' + data.Key + ' Value: ' + data.Value + ' Delete Success')
						except ObjectDoesNotExist:
							result[tuple[0]] = 'KeyNotFound'
							database_logger.info('Key: ' + tuple[0] + ' Delete Failure')
				return HttpResponse(json.dumps(result).encode('utf-8'), mimetype='application/json')
			except Exception:
				exc_info = str(sys.exc_info()[0])
				site_logger.error('Unexpected error: ' + exc_info)
				return HttpResponse(cgi.escape('Unexpected error' + exc_info), mimetype=None, status=200)
		else:
			'''*****************************************************************************
			Display 404
			PATH: webapp.views.site.get; METHOD: not post; PARAMS: none; MISC: none;
			*****************************************************************************'''
			raise Http404
