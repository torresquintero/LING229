#include <boost/python.hpp>
BOOST_PYTHON_MODULE(hello_ext){
	using namespace boost::python;
	def("hal", hal)
}

char cosnt* hal(){
	return "sorry i can't do that dave...";
}


