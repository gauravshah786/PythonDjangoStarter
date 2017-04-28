import web

urls = (
	'/hello', 'Index',
	'/upload', 'Upload'
	)

app = web.application(urls,globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(elf):
		return render.hello_form()

	def POST(self):
		form = web.input(name = "Nobody", greet = "Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

class Upload:
	def GET(self):
		return render.file_upload_form()

	def POST(self):
		x = web.input(myfile={})
		filedir = '/home/gaurav/workspace/pythonProject/fileStore'
		if 'myfile' in x:
			filepath = x.myfile.filename.replace('\\','/')
			filename = filepath.split('/')[-1]
			fout = open(filedir +'/'+ filename,'w')
			fout.write(x.myfile.file.read())
			fout.close()
		raise web.seeother('/upload')

if __name__ == '__main__':
	app.run()