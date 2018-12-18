# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import time

from flask import Flask, redirect, url_for
import opencensus.trace.exporters.stackdriver_exporter
import opencensus.trace.tracer


exporter = opencensus.trace.exporters.stackdriver_exporter.StackdriverExporter()
tracer = opencensus.trace.tracer.Tracer(exporter=exporter)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('index'))


@app.route('/index.html', methods=['GET'])
def index():
    tracer.start_span(name='index')

    # Add up to 1 sec delay, weighted toward zero
    time.sleep(random.random() ** 2)
    result = "Tracing requests"

    tracer.end_span()
    return result
