import httplib
import json
import time

class JenkinsStatus:
	SUCCESS = "SUCCESS"
	FAILURE = "FAILURE"
	UNAVAILABLE = "UNAVAILABLE"
	UNKNOWN = "UNKNOWN"

	def __init__(self, host, port, build):
		self.endpoint = self.__get_endpoint_for_build(build)
		self.host = host
		self.port = port

	def get_status(self):
		response = self.__get(self.host, self.port, self.endpoint)
		status = self.__parse_response(response)
		print status
		return status

	def __get(self, host, port, endpoint):
	    conn = None
	    try:
		conn = httplib.HTTPConnection(host, port, 2)
		conn.request("GET", endpoint)
		response = conn.getresponse()
		return {"status": response.status,
			"reason": response.reason,
			"body": response.read()}
	    except:
		return None
	    finally:
		if conn is not None:
		    conn.close()

	def __get_endpoint_for_build(self, build):
	    return "/job/{}/lastBuild/api/json?pretty=true&tree=result".format(build)

	def __parse_response(self, response):
	    if self.__is_unavailable(response):
		return JenkinsStatus.UNAVAILABLE
	    return self.__get_build_result(response)

	def __is_unavailable(self, response):
	    if response is None:
		return True
	    if (response.get("status") != 200):
		return True
	    return False

	def __get_build_result(self, response):
	    body = response.get("body")
	    result = json.loads(body).get("result", "")
	    if result in [JenkinsStatus.SUCCESS, JenkinsStatus.FAILURE]:
		return result
	    return JenkinsStatus.UNKNOWN
