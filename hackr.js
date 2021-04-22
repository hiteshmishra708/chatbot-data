function getAnswer(children, count) {
	answer = []
	for (i=count+1; i<children.length; i++) {
		child = children[i]
		if (child.nodeName == "H4") break;
		else answer.push(child.innerText)
	}
	return answer.join("\n")
}

content = document.getElementsByClassName("content")[0]
questions = []
for (let i=8; i<content.children.length; i++) {
	child = content.children[i]
	if(child.nodeName == "H4") {
		questions.push({
			question: child.innerText,
			answer: getAnswer(content.children, i)
		})
	}
}
console.log(JSON.stringify(questions))

// node link https://hackr.io/blog/node-js-interview-questions
// java link https://hackr.io/blog/java-interview-questions
// python link https://hackr.io/blog/python-interview-questions