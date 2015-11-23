Inpired by "Workshop Apps Alta Performance" from @aoqfonseca

Simple performance tests python's web frameworks.

*Testes under localhost, to eliminate newtork latency.*

Some tests are from http://computers-are-fast.github.io/

Conversamos sobre o triângulo da perfomance (concorrência, vazão e latência) e como ele nos ajuda a definir as estratégias que vamos adotar na resolução dos problemas.

Vimos que não existe uma fórmula. Existe alguns caminhos que já foram trilhados e que costumam resolver os problemas, como por exemplo: filas, cache L1 e L2,  varnish, nginx com modo stale,  cdn's, etc.

Other frameworks:
http://morepath.readthedocs.org/en/latest/
http://pyramid-blogr.readthedocs.org/en/latest/

Apache benchmark:
ab -n 1000 -c 50 http://10.0.1.27:3000/?name=andre
ab -n 1000 -c 50 http://10.0.1.90:8080/workshop/hello/andre

jmeter
http://newrelic.com/sp/python-monitoring
https://github.com/Pylons/pyramid_debugtoolbar
https://docs.python.org/2/library/profile.html
http://wsgi.readthedocs.org/en/latest/
https://www.python.org/dev/peps/pep-0333/
http://wsgi.tutorial.codepoint.net/
https://www.devside.net/wamp-server/load-testing-apache-with-ab-apache-bench


== Simple Hello World Applications ==

Receives a name by URL, and returns "Hello World, {}!".format(name)

=== Flask ===

ab -n 1000 -c 500 http://127.0.0.1:5000/guido
Requests per second:    1098.90 [#/sec] (mean)

=== Bottle ===

ab -n 1000 -c 500 http://127.0.0.1:5000/guido
Strange things happen after 900 requests... (CTRL+C on test script, after it took too long)

Time taken for tests:   45.259 seconds
Complete requests:      998
Requests per second:    22.05 [#/sec] (mean)

=== Pyramid ===

ab -n 1000 -c 500 http://127.0.0.1:5000/guido
Strange things happen after 900 requests... (CTRL+C on test script, after it took too long)

Time taken for tests:   10.911 seconds
Complete requests:      999
Requests per second:    91.56 [#/sec] (mean)
