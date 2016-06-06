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

from __init__ import *
from iAS.core.appmgt import appDAO
from random import randint
from iAS.core.devicemgt.DeviceDAO import *


class Main(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        if 'User' in session:
            return make_response(
                redirect('/applications')
            )
        else:
            return make_response(
                render_template('login.html'),
                200, headers)


class Applications(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}

        if 'User' in session:
            username = session['User']['userName']
            profilePicture = session['User']['profilePicture']
            appList = appDAO.getAppList()

            return make_response(
                render_template('applications/applications.html',
                                username = username,
                                profilePicture = profilePicture,
                                appList = appList
                                ),
                200, headers
            )
        else:
            return make_response(
                redirect('/login')
            )


class Application_Render(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        if 'User' in session:
            username = session['User']['userName']
            profilePicture = session['User']['profilePicture']
            appDetais = appDAO.getAppDetailsById(id)

            return make_response(
                render_template('applications/application.html',
                                username=username,
                                profilePicture=profilePicture,
                                appDetails=appDetais
                                ),
                200, headers
            )
        else:
            return make_response(
                redirect('/login')
            )


class EnrolledApps(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}

        if 'User' in session:
            username = session['User']['userName']
            profilePicture = session['User']['profilePicture']
            dao = DeviceDAO()
            deviceList = dao.getDevices(username)

            return make_response(
                render_template('apps/enrolledapps.html',
                                username=username,
                                profilePicture=profilePicture,
                                devices=deviceList),
                200, headers)
        else:
            return make_response(
                redirect('/login')
            )


class Enrolled_App_Render(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        if 'User' in session:
            username = session['User']['userName']
            profilePicture = session['User']['profilePicture']

            return make_response(
                render_template('apps/sample_app/sample_app.html',
                                username = username,
                                profilePicture = profilePicture
                                ),
                200, headers
            )
        else:
            return make_response(
                redirect('/login')
            )


class TemperatureGen(Resource):
    def get(self):
        temperature = randint(27, 29)
        return make_response(
                jsonify({'temperature': temperature}),
                200
        )