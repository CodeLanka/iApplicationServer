# Copyright 2016 Team - iAS, University Of Peradeniya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import zipfile

from __init__ import *
from iAS.core.devicemgt.EnrollDevice import downloadAgent

app = Flask(__name__)
api = Api(app)


api.add_resource(Main, '/')

api.add_resource(Applications, '/applications')
api.add_resource(Application_Render, '/applications/<id>')
api.add_resource(EnrolledApps, '/enrolledapps')
api.add_resource(Render_Sample_App_Page, '/enrolledapps/<id>')
api.add_resource(Sample_App_Set_Status, '/enrolled_apps/sample_app/<status>')
api.add_resource(TemperatureGen, '/enrolledapps/ajax/getdata')
# api.add_resource(messageHandler, '/sendMessage')


api.add_resource(Login, '/login')


@app.route('/callback')
@google.authorized_handler
def authorized(resp):
    session['access_token'] = resp['access_token']
    getUserInfo(session["access_token"])
    session["User"] = json.loads(getUserJson())
    return redirect('/')


@google.tokengetter
def get_access_token():
    return session.get('access_token')

@app.route('/applications/downloads')
def download():
    userName = session["User"]["userName"]
    deviceName = request.args['app-name']
    deviceId = request.args['appid']
    archive = zipfile.ZipFile(downloadAgent(userName, deviceName, deviceId), 'r')
    print(userName)
    archive.close()
    return Response(archive,
                    mimetype='application/zip',
                    headers={'Content-Disposition': 'attachment; filename=agent.zip'})


