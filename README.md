# coding-agent-cli
更新学习中，目前实现：

五个命令，通过/help查看所有命令

把 run_sync() 换成 agent.iter() 来实现 Agent 循环的逐步输出

分析环境错误（透明重试） or 模型行为错误（错误送进上下文）。增加 API、工具和主循环三层错误处理。